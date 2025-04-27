import os
import numpy as np
from openai import OpenAI
from scipy.stats import trim_mean
from scipy.signal import savgol_filter

def get_llmtime_predictions(prompt, num_samples=20, temperature=0.7, num_predictions=40):
    """Get predictions from LLMTime with improved prompt engineering."""
    try:
        # Ensure API key is properly set
        if not os.getenv('OPENAI_API_KEY'):
            raise ValueError("OPENAI_API_KEY environment variable not set")
            
        # Format the prompt according to the paper with improved context
        system_prompt = """You are a time series forecasting model. Given a sequence of numbers, predict the next values in the sequence. 
        The numbers are normalized between 0 and 1. Consider the following:
        1. Look for patterns and trends in the data
        2. Consider seasonal variations if present
        3. Account for any recent changes in the trend
        4. Return your predictions as a comma-separated list of numbers between 0 and 1.
        Do not include any explanations or additional text, just the numbers."""
        
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        response = client.chat.completions.create(
            model="gpt-4",  # Using GPT-4 for better performance
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            n=num_samples,
            max_tokens=1000
        )
        
        predictions = []
        for choice in response.choices:
            try:
                content = choice.message.content.strip()
                # Clean the response
                content = content.replace('[', '').replace(']', '')
                content = content.replace('\n', '')
                # Parse numbers
                values = [float(x.strip()) for x in content.split(',') if x.strip()]
                # Ensure values are in [0,1] range
                values = [max(0, min(1, x)) for x in values]
                if len(values) == num_predictions:
                    predictions.append(values)
            except (ValueError, AttributeError) as e:
                print(f"Warning: Error parsing prediction: {e}")
                continue
                
        if not predictions:
            print("Warning: No valid predictions obtained from LLMTime")
            return None
            
        return np.array(predictions)
        
    except Exception as e:
        print(f"Error getting LLMTime predictions: {e}")
        return None

def optimize_llmtime_parameters(train, test, window_sizes=[40, 60], temperatures=[0.05, 0.1], 
                              num_samples_list=[16], smoothing_windows=[5, 7]):
    """Optimize LLMTime parameters using grid search."""
    best_error = float('inf')
    best_params = None
    best_predictions = None
    
    for window_size in window_sizes:
        for temp in temperatures:
            for num_samples in num_samples_list:
                for agg_method in ['median', 'trimmed_mean']:
                    print(f"Trying window={window_size}, temp={temp}, num_samples={num_samples}, agg={agg_method}...")
                    rolling_train = train[-window_size:]
                    formatted_rolling, scaler, context = preprocess_time_series(rolling_train)
                    
                    prompt = f"""Context: {context}

Given the following sequence of {len(formatted_rolling)} normalized weekly values:
{', '.join(formatted_rolling)}

This data is from a real-world financial time series with both trend and seasonality.
Your goal is to minimize the root mean squared error (RMSE) of your predictions.
Please predict the next {len(test)} normalized values in the sequence, considering:
- Recent trends and changes
- Seasonal patterns (e.g., annual or quarterly cycles)
- Any abrupt shifts or anomalies
Minimize prediction error. Match the statistical properties of the sequence. Avoid abrupt jumps unless the data shows a clear anomaly.

Return only the predicted numbers, separated by commas, with no explanation or extra text."""

                    llmtime_samples = get_llmtime_predictions(
                        prompt,
                        num_samples=num_samples,
                        temperature=temp,
                        num_predictions=len(test)
                    )
                    
                    if llmtime_samples is not None:
                        if agg_method == 'median':
                            llmtime_agg = np.median(llmtime_samples, axis=0)
                        else:
                            llmtime_agg = trim_mean(llmtime_samples, proportiontocut=0.1, axis=0)
                            
                        # Inverse transform and clip
                        llmtime_agg = scaler.inverse_transform(llmtime_agg.reshape(-1, 1)).flatten()
                        llmtime_agg = np.clip(llmtime_agg, train.min(), train.max())
                        
                        # Try several smoothing window lengths
                        for smooth_win in smoothing_windows:
                            if len(llmtime_agg) > smooth_win:
                                llmtime_smoothed = savgol_filter(llmtime_agg, smooth_win, 2)
                            else:
                                llmtime_smoothed = llmtime_agg
                                
                            error = np.sqrt(np.mean((test.values - llmtime_smoothed) ** 2))  # RMSE
                            
                            if error < best_error:
                                best_error = error
                                best_params = {
                                    'window_size': window_size,
                                    'temperature': temp,
                                    'num_samples': num_samples,
                                    'agg_method': agg_method,
                                    'smoothing_window': smooth_win
                                }
                                best_predictions = llmtime_smoothed
                                
    return best_predictions, best_params, best_error 