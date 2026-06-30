import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

# Get credentials
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_SERVICE_KEY')
bucket = os.getenv('SUPABASE_STORAGE_BUCKET', 'csv-uploads')

print(f'🔍 Testing Supabase Connection...')
print(f'URL: {url}')
print(f'Key: {key[:20]}...' if key else 'Key: MISSING')
print(f'Bucket: {bucket}')

if not url or not key:
    print('❌ Missing Supabase credentials in .env file')
    exit(1)

try:
    # Create client
    supabase = create_client(url, key)
    print('✅ Supabase client created')
    
    # List buckets
    buckets = supabase.storage.list_buckets()
    print(f'📦 Found {len(buckets)} buckets:')
    for b in buckets:
        print(f'  - {b.name}')
    
    # Check if our bucket exists
    bucket_exists = any(b.name == bucket for b in buckets)
    if bucket_exists:
        print(f'✅ Bucket "{bucket}" exists')
    else:
        print(f'❌ Bucket "{bucket}" does NOT exist')
        print('Creating bucket...')
        supabase.storage.create_bucket(bucket, {'public': False})
        print(f'✅ Bucket "{bucket}" created')
    
    # Test upload
    print('\n📤 Testing upload...')
    test_content = b'id,name\n1,Test\n2,Data'
    result = supabase.storage.from_(bucket).upload(
        'test_upload.csv',
        test_content,
        file_options={'content-type': 'text/csv'}
    )
    print(f'✅ Upload successful!')
    print(f'   Result: {result}')
    
    # Clean up test file
    supabase.storage.from_(bucket).remove(['test_upload.csv'])
    print('✅ Test file cleaned up')
    
except Exception as e:
    print(f'❌ Error: {e}')
