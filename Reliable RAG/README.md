# 📄 Self-RAG

## Overview

This project implements a **Self-RAG pipeline**.  
[reference Self-RAG (https://arxiv.org/abs/2310.11511)]
Unlike traditional RAG, this pipeline introduces **Document Grading**, **Query Transformation**, **Relevance Check** and **Hallucination Check**  steps to generate **more accurate and reliable answers**.

The pipeline uses the **Samsung Electronics 2024 Sustainability Report (Korean version)** as the knowledge base.

---

## Key Features

- **Document Grading:**  
  a grader assessing relevance of a retrieved document to a user question..

- **Query Transformation:**  
  a question re-writer that converts an input question to a better version that is optimized for vectorstore retrieval
  
- **Hallucination Check:**  
  a grader assessing whether an LLM generation is grounded in supported by a set of retrieved facts.

- **Relevance Check:**  
  a grader assessing whether an answer addresses and resolves a question

- **Iterative Improvement:**  
  Through document grading and query refinement, the model continuously improves the answer quality.

---

## Pipeline Structure
![RAG_pipeline](https://github.com/user-attachments/assets/e4381679-b111-4329-8be5-97d939180a85)

---

## Context

- 📚 **Samsung Electronics Sustainability Report 2024 (Korean)**
- The data is indexed into an internal vector store (FAISS) for retrieval.
