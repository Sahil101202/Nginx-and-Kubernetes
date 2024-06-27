import requests
import os
import time
import matplotlib.pyplot as plt

# Nginx service URL
NGINX_URL = "http://127.0.0.1:61406/classify"  # Replace with your Nginx service URL

def upload_image(image_path):
    try:
        with open(image_path, 'rb') as f:
            files = {'image': f}
            response = requests.post(NGINX_URL, files=files)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"HTTP error! Status: {response.status_code}")
                return None

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def store_results(results):
    with open("results.txt", "w") as f:
        for filename, status, response_time in results:
            f.write(f"{filename},{status},{response_time}\n")



if __name__ == "__main__":
    IMAGES_DIR = "/Users/sahilnakrani/Desktop/os_project/Nginx-and-Kubernetes/testing/images"  # Replace with your images directory
    results = []

    for filename in os.listdir(IMAGES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".bmp"):
            image_path = os.path.join(IMAGES_DIR, filename)
            print(f"Uploading image: {filename}")
            start_time = time.time()
            result = upload_image(image_path)
            end_time = time.time()

            if result:
                print("Classification result:")
                for prediction in result:
                    probability_percentage = round(prediction['probability'] * 100, 2)
                    print(f"{prediction['label']}: {probability_percentage}%")
                
                # Store result and response time
                results.append((filename, "Success", round(end_time - start_time, 2)))
            else:
                print("Classification failed.")
                results.append((filename, "Failed", None))

            print("------------------------")
            time.sleep(1)  # Optional delay between uploads

    # Store results in a file
    store_results(results)

    # Print summary
    print("\nSummary:")
    for filename, status, response_time in results:
        if status == "Success":
            print(f"{filename}: {status}, Response Time: {response_time} seconds")
        else:
            print(f"{filename}: {status}")

    
