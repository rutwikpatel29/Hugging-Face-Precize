# Hugging-Face-Precize
Hugging Face Report Generator, This project contains a Docker container that periodically generates reports by fetching data from the Hugging Face model hub, compiling a list of the top 10 downloaded models.
# Hugging Face Report Generator

This project contains a Docker container that periodically generates reports by fetching data from the Hugging Face model hub, compiling a list of the top 10 downloaded models.

## Getting Started

### Prerequisites

- Docker

### Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/huggingface_report.git
    cd huggingface_report
    ```

2. Build the Docker image:
    ```sh
    docker build -t huggingface_report .
    ```

3. Run the Docker container:
    ```sh
    docker run --rm -v $(pwd)/reports:/reports huggingface_report
    ```

### Notes

- The generated report will be available in the `reports` directory.

## License

This project is licensed under the MIT License.
