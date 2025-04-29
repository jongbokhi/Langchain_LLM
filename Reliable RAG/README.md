# 📄 Graded RAG Pipeline (Inspired by Adaptive RAG)

## Overview

This project implements a **custom Retrieval-Augmented Generation (RAG) pipeline** inspired by the Adaptive RAG structure.  
Unlike traditional RAG, this pipeline introduces **Document Grading** and **Query Transformation** steps to generate **more accurate and reliable answers**.

The pipeline uses the **Samsung Electronics 2024 Sustainability Report (Korean version)** as the knowledge base.

---

## Key Features

- **Document Grading:**  
  Retrieved documents are evaluated, and irrelevant documents are filtered out.

- **Query Transformation:**  
  If retrieved documents are not sufficiently relevant, the original query is rephrased and retrieval is retried.

- **Hallucination Handling:**  
  If the generated answer is inaccurate or hallucinated, the retrieval and generation process is repeated.

- **Iterative Improvement:**  
  Through document grading and query refinement, the model continuously improves the answer quality.

---

## Pipeline Structure
![RAG_pipeline](https://github.com/user-attachments/assets/e4381679-b111-4329-8be5-97d939180a85)

---

## Context

- 📚 **Samsung Electronics Sustainability Report 2024 (Korean)**
- The data is indexed into an internal vector store (FAISS) for retrieval.
