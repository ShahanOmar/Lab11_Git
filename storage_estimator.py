# storage_estimator.py
# Lab 11: Basic Storage Estimator

def estimate_storage():
    print("--- Storage Requirement Estimator ---")
    
    try:
        # Gather user inputs
        num_records = int(input("Enter total number of records: "))
        avg_record_size_bytes = int(input("Enter average size per record (in bytes): "))
        
        # Calculate total size
        total_bytes = num_records * avg_record_size_bytes
        total_mb = total_bytes / (1024 * 1024)
        
        # Display results
        print("\n--- Estimation Results ---")
        print(f"Total Size: {total_bytes:,} Bytes")
        print(f"Total Size: {total_mb:.2f} MB")
        print(f"Total Size: {(total_mb / 1024):.4f} GB")
        print(f"Total Size: {(total_mb / (1024 * 1024)):.6f} TB")
        
    except ValueError:
        print("Error: Please enter numbers only.")

if __name__ == "__main__":
    estimate_storage()
