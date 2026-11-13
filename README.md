# CS50P Study Notes Mini-RAG
#### Video Demo:  <URL HERE>
#### Description:

**CS50P Study Notes Mini-RAG** is a command-line interface (CLI) application built in Python that implements a local Retrieval-Augmented Generation (RAG) pipeline over personal study notes written in Markdown (`.md`) and plain text (`.txt`). Designed to help students query their own Portuguese study materials from Harvard's CS50P course, the tool combines classical information retrieval techniques—specifically TF-IDF vectorization and cosine similarity via `scikit-learn`—with Google's Gemini LLM (`google-genai`) to generate accurate, grounded, and source-cited answers directly in the terminal.

### Project Structure and Files

The project directory consists of the following core files:

- **`project.py`**: The main entry point of the application containing the interactive CLI workflow (`main()`) and seven modular helper functions that execute each stage of the RAG pipeline (`load_notes`, `split_into_chunks`, `rank_chunks`, `is_relevant`, `build_prompt`, `ask_llm`, and `evaluate`).
- **`test_project.py`**: The automated unit test suite built with `pytest`. It thoroughly tests the data ingestion, text chunking, TF-IDF ranking, relevance filtering, prompt construction, and top-3 retrieval evaluation completely offline, without consuming external API quotas.
- **`notas/`**: The directory storing the Markdown study notes (such as `semana-00-funcoes-e-variaveis.md`), organized with `#` and `##` headings.
- **`requirements.txt`**: Lists all external third-party dependencies required to run and test the project (`scikit-learn`, `google-genai`, `python-dotenv`, and `pytest`).
- **`.env` & `.gitignore`**: Environment configuration used to safely load the `GEMINI_API_KEY` locally while preventing sensitive credentials from being tracked by Git.

### Pipeline Architecture and Functions

1. **`load_notes(folder)`**: Uses `pathlib.Path` to validate whether the target folder exists and searches for all `.md` and `.txt` files using `.glob()`. If the folder does not exist or contains no valid files, it gracefully terminates execution via `sys.exit()`. Otherwise, it returns a list of dictionaries containing each file's `"source"` name and `"text"` content.
2. **`split_into_chunks(text, source, max_chars=500)`**: Splits raw Markdown documents into smaller, semantically cohesive sections using regular expressions (`re.split(r"^## ", text, flags=re.MULTILINE)`). If a section's body exceeds `max_chars`, the function further subdivides the text by paragraphs (`\n\n`) while preserving a one-paragraph overlap (`atual = [atual[-1], p]`) so context is never abruptly lost between boundaries.
3. **`rank_chunks(question, chunks, k=3)`**: Converts both the study chunks and the user's question into numerical vectors using `TfidfVectorizer` configured with a custom list of Portuguese stopwords (`STOPWORDS_PT`). It then calculates the `cosine_similarity` between the question vector and all chunk vectors, attaches the resulting similarity `"score"` to each chunk dictionary, and returns the top `k` highest-scoring chunks sorted in descending order.
4. **`is_relevant(results, threshold=0.1)`**: Acts as a gatekeeper before calling the external LLM API. It checks whether the results list is non-empty and verifies if the highest similarity score (`results[0]["score"]`) meets or exceeds the minimum `threshold` (`0.1`).
5. **`build_prompt(question, chunks)`**: Formats the retrieved chunks into an enumerated reference block inside `<trechos>` XML-like tags (`[1] source › section: "text"`) and combines them with system instructions that strictly forbid the LLM from using external knowledge, enforcing inline citations (`[n]`).
6. **`ask_llm(prompt)`**: Loads the `GEMINI_API_KEY` from the `.env` file using `python-dotenv`, initializes the `genai.Client`, and sends the grounded prompt to the `gemini-3.5-flash-lite` model, returning the generated response text.
7. **`evaluate(chunks, cases)`**: An offline benchmarking function that takes a list of test cases (`{"question": ..., "expected_source": ...}`) and measures the retrieval system's Top-3 accuracy (`float` between `0.0` and `1.0`). Users can trigger this evaluation directly from `main()` by typing `--eval` at the prompt.

### Design Choices

Several deliberate architectural decisions were made during development:
- **Hybrid Local + Cloud Approach (Gatekeeper Pattern)**: Calling an LLM API for every single terminal input can be slow and costly, especially when a user asks an off-topic question unrelated to the study notes. By placing `rank_chunks` (local TF-IDF) and `is_relevant` in front of `ask_llm`, irrelevant queries are immediately intercepted locally with zero API cost.
- **Isolation of External I/O for Testability**: The `build_prompt` and `ask_llm` steps were intentionally separated into two distinct functions. This allowed `test_project.py` to validate prompt engineering rules and citation formatting deterministically via `pytest` without requiring internet access or mocking complex network calls.
- **Paragraph Overlap in Chunking**: Simply slicing text at a rigid 500-character mark often breaks code blocks or explanations in half. Splitting by Markdown `##` headers first, followed by paragraph-level grouping with a 1-paragraph sliding window overlap, keeps explanations intact and improves TF-IDF matching accuracy.