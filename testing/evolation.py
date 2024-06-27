import matplotlib.pyplot as plt

def load_results(file_path):
    results = []
    with open(file_path, "r") as f:
        next(f)  # Skip header
        for line in f:
            filename, status, response_time = line.strip().split(',')
            if response_time == 'None':
                response_time = None
            else:
                response_time = float(response_time)
            results.append((filename, status, response_time))
    return results

def plot_response_times(results):
    response_times = [response_time for _, _, response_time in results if response_time is not None]

    plt.figure(figsize=(10, 6))
    plt.plot(response_times, marker='o', linestyle='-', color='b')
    plt.xlabel('Image Uploads')
    plt.ylabel('Response Time (seconds)')
    plt.title('Response Time per Image Upload')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('response_times.png')
    plt.show()

def plot_success_failure_pie(results):
    successes = sum(1 for _, status, _ in results if status == "Success")
    failures = len(results) - successes

    labels = 'Success', 'Failure'
    sizes = [successes, failures]
    colors = ['green', 'red']
    explode = (0.1, 0)

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Success vs Failure Rate')
    plt.savefig('success_failure_pie.png')
    plt.show()
    

if __name__ == "__main__":
    # Load results from file
    results = load_results("results.txt")

    # Plot response times
    plot_response_times(results)

    # Plot success vs failure rate
    plot_success_failure_pie(results)
