# Agentic Retrieval-Augmented Generation(RAG) for Industry Classification 

This project explores how **Agentic Retrieval-Augmented Generation (RAG)** can be applied to enrich business dataset attributes. 
Specifically, it focuses on determining the **Industry Classification** of companies based on their names while adhering to the **GLOBAL INDUSTRY CLASSIFICATION STANDARD**.  

---

## Problem Statement  

The task involves enriching each row of a dataset by classifying companies into their respective industries. The attributes to be derived include:  

- **Legal Entity Identifier (LEI)**  
- **Entity Type**  
- **Industry Classification**  
- **Company Size**  

### Initial Attempts  

Previous attempts at solving this problem involved techniques like:  
- **Pre-trained DistilBERT**  
- **Zero-shot Classification (Facebook BART-large-MNLI)**  
- **XGBoost**  

However, these methods showed unsatisfactory performance.
**[result](https://github.com/jongbokhi/problem-set_Forward-Analytics)**
---

## Alternative: Agentic Retrieval-Augmented Generation (RAG)  

To overcome the challenges, this project leverages **Agentic RAG** with the following components:  

### LLM and Tools  

1. **LLM Selection**  
   - **GPT-4o**   

2. **Integrated Tools**  
   - **PythonAstREPLTool**: Executes Python code dynamically during runtime.  
   - **PDF Document Retrieval Tool**: Extracts relevant information from reference documents like the GICS methodology PDF.  
   - **Search Tool**: Implements **TavilySearchResults** for efficient web-based searches.  

---

### Methodology  

1. **Contextual Reference**  
   - The **GLOBAL INDUSTRY CLASSIFICATION STANDARD (GICS®) METHODOLOGY PDF** was provided as a key contextual document to ensure adherence to industry classification standard.  
   - **[Source](https://www.msci.com/our-solutions/indexes/gics)**
2. **Prompt Engineering**  
   - A DataFrame containing company names was fed into the system.  
   - Prompts were carefully crafted to guide the LLM and tools to:  
     - Search the web for each company’s industry classification.  
     - Verify the retrieved classification against the GICS methodology.  
     - Assign the final classification to the dataset.  

3. **Experimentation**  
   - The approach was tested on the top 30 rows of the dataset to validate the workflow and assess performance.  

---

## Results  

The experiment yielded **highly satisfactory results**, with significant improvements over previous methods. By combining:  
- **Search tools** for real-time data retrieval,  
- **Document retrieval** for standards compliance, and  
- **LLM capabilities** for reasoning and decision-making,  

---

## Future Work  

This project provides a scalable foundation for automated data enrichment. Future enhancements include:  
- Extending the classification to larger datasets.  
- Adding **real-time APIs** for fetching updated company data.
