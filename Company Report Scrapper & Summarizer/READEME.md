# 📰 Intelligent Company Report Scraper & Summarizer

This task builds a **press release scraper** and **intelligent report analyzer** for three companies: **AcouSort**, **Carlsberg**, and **Stockwik**. It supports both static and JavaScript-rendered websites and leverages a Large Language Model (LLM) to identify and classify quarterly and annual reports. It also performs real-time search using the **SERP API** to generate a final summary report for each company.

---

## 🔄 Workflow Overview

### 1. 🧩 Scrap Chain: Press Release Extraction

- **Stockwik (JavaScript-rendered)**  
  - Uses **Selenium** to load and render JavaScript content from  
    `https://www.stockwik.se/pressmeddelanden`.
  - Saves the fully rendered HTML locally and loads it using `BSHTMLLoader` to create `Document` objects.

- **AcouSort & Carlsberg (Static HTML)**  
  - Uses **LangChain’s `WebBaseLoader`** and `BeautifulSoup` with `SoupStrainer` to extract press release sections.
  - Targets only relevant containers such as `div.mfn-list` and `div.news-list__result-records`.

- All press releases are merged into a list called `scrapped_info`.

---

### 2. 🧠 Report Chain: LLM-based Report Classification

- Each press release is passed through an **LLM chain**.
- The model identifies whether the report is **quarterly or annual**, and extracts:
  - `company`
  - `report_name`
  - `report_type`
  - `date`
  - `link`
- The outputs are structured using a **`Pydantic` model (`ReportScraper`)**, and grouped into a `ReportScraperCollection`.

---

### 3. 🌐 Company Summary: Real-time Web Search with SERP API

- For each company, a **real-time Google search** is performed using the **SERP API**.
- The LLM takes both:
  - Extracted report data
  - SERP search results  
  and generates a **human-readable company report**.
- The final output is presented in a **report-style summary**.

---

## ⚙️ Key Tools

| Tool / Library     | Purpose                                      |
|--------------------|----------------------------------------------|
| **Selenium**       | Render JavaScript-based websites             |
| **LangChain**      | LLM chain construction & document loading    |
| **BeautifulSoup**  | HTML parsing and filtering                   |
| **OpenAI GPT**     | Text understanding and report generation     |
| **Pydantic**       | Structured and validated output models       |
| **SERP API**       | Real-time company information via Google     |

---
