# LLM-Powered Question Answering System

This project implements a question-answering system using a pre-trained BERT large language model.  It takes a question and a context paragraph as input and returns the answer extracted from the context.

## Project Setup

To set up the project locally, follow these steps:

1. **Prerequisites:**
    * Python 3.9+
    * `transformers`
    * `torch`
    * `pytest`

2. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/LLM-Implementation.git
    ```

3. **Navigate to the project directory:**
    ```bash
    cd LLM-Implementation
    ```

4. **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Configuration:** Download the pre-trained BERT model weights. This will happen automatically the first time you run the script if the model isn't found locally.



## Running the Project

To run the project, follow these instructions:

1. **Activate the virtual environment (if used):**
    ```bash
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

2. **Run the main script:**
    ```bash
    python main.py --question "What is the capital of France?" --context "France is a country in Europe. Paris is its capital city."
    ```
    * Use the `--question` flag to specify the question.
    * Use the `--context` flag to provide the context paragraph.
    * You can also provide input from files using  `--question_file <path>` and `--context_file <path>`.

3. **Expected Output:**
    * The answer will be printed to the console. For the example above, the output would be "Paris".


## Testing

To run the tests:

1. **Navigate to the tests directory:**
    ```bash
    cd tests
    ```
2. **Run the test suite:**
    ```bash
    pytest
    ```



## Deployment (Optional)

This project can be deployed as a web service using Flask or FastAPI.  See the `deployment` directory for example deployment configurations.


## Contributing

Contributions are welcome!  Please follow PEP 8 coding style guidelines.  Use a feature branch workflow for your changes and submit a pull request.



## License


This project is licensed under the MIT License. A `LICENSE` file is included in the root of this repository.
