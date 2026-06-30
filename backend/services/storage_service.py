import os
import uuid
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Tuple, Optional
from fastapi import UploadFile
import io

# Initialize uploads directory
os.makedirs('uploads', exist_ok=True)

async def save_csv_upload_for_user(file: UploadFile, user_id: str) -> Tuple[str, str, pd.DataFrame]:
    '''Save CSV locally'''
    try:
        # Read file
        content = await file.read()
        
        # Parse CSV
        try:
            df = pd.read_csv(io.StringIO(content.decode('utf-8')))
        except Exception as e:
            raise ValueError(f'Invalid CSV format: {str(e)}')
        
        if df.empty:
            raise ValueError('CSV file is empty')
        
        # Generate IDs
        dataset_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'uploads/{user_id}_{dataset_id}_{timestamp}_{file.filename}'
        
        # Save locally
        with open(filename, 'wb') as f:
            f.write(content)
        
        print(f'File saved locally: {filename}')
        print(f'Rows: {len(df)}, Columns: {len(df.columns)}')
        
        return dataset_id, filename, df
        
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f'Error processing upload: {str(e)}')

def get_dataframe(file_path: str) -> Optional[pd.DataFrame]:
    '''Load dataframe from stored file path'''
    try:
        if not os.path.exists(file_path):
            return None
        return pd.read_csv(file_path)
    except Exception as e:
        print(f'Error loading dataframe: {e}')
        return None

def load_dataframe_from_path(dataset_id: str, stored_path: str) -> pd.DataFrame:
    '''Load dataframe from path, raise error if fails'''
    try:
        if not os.path.exists(stored_path):
            raise FileNotFoundError(f'File not found: {stored_path}')
        df = pd.read_csv(stored_path)
    except Exception as e:
        raise ValueError(f'Failed to load dataframe: {str(e)}')

    return df


def get_columns(file_path: str) -> list:
    '''Get column names from CSV'''
    try:
        df = get_dataframe(file_path)
        if df is not None:
            return df.columns.tolist()
        return []
    except Exception:
        return []

def get_row_count(file_path: str) -> int:
    '''Get row count from CSV'''
    try:
        df = get_dataframe(file_path)
        if df is not None:
            return len(df)
        return 0
    except Exception:
        return 0
