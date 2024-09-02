# LangChain Translation Example

This repository demonstrates a simple translation example using LangChain. The script takes input text in English and translates it into a specified target language using OpenAI's language model.

## Prerequisites

- Python 3.7+
- An OpenAI API key
- Environment variables set up for `OPENAI_API_KEY` and `OPENAI_API_HOST`

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vinodvpillai/your-repository.git
cd your-repository
```

### 2. Install Required Packages

Make sure you have `langchain-core`, `langchain-openai`, and `python-dotenv` installed:

```bash
pip install langchain-core langchain-openai python-dotenv
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_HOST=https://api.openai.com
```

Replace `your_openai_api_key` with your actual OpenAI API key.

### 4. Run the Script

You can run the script using Python:

```bash
python translation_example.py
```

## Explanation

The script performs the following steps:

1. **Load Environment Variables**: It loads the API key and host URL from a `.env` file.
   
2. **Define the Prompt**: It uses a `ChatPromptTemplate` to define a prompt template for translating text from English into a specified target language.

3. **Initialize the LLM Model**: It initializes the `ChatOpenAI` model using the provided API key and base URL.

4. **Output Parser**: The `StrOutputParser` is used to parse the output of the model.

5. **Chain**: The prompt, model, and parser are chained together to perform the translation.

6. **Invoke the Chain**: Finally, the chain is invoked with the input text and target language. In this example, the text `"hi"` is translated into Italian.

## Example Output

When you run the script, you should see an output similar to:

```bash
"ciao"
```

## Customization

- You can change the input text or target language by modifying the `chain.invoke()` parameters.

```python
print(chain.invoke({"language": "french", "text": "hello"}))
```

This would translate "hello" into French.

## Contributing

Feel free to open issues or submit pull requests if you want to improve or add new features to this example.

## License

This project is licensed under the MIT License.
