## LogFlow Sketcher

An educational implementation of real-time log analytics using the Space-Saving algorithm. This project demonstrates how theoretical computer science principles solve practical engineering problems in observability and monitoring systems.

<hr>

## Educational Purpose

This project demonstrates how **theoretical computer science** enables **practical systems** that are both **efficient** and **provably correct**. We implement the Space-Saving algorithm not just as code, but as a vehicle for understanding deep algorithmic principles.


## Learning Objectives

After studying this implementation, you should understand:

- **Streaming Algorithm Design:** How to process infinite data with finite memory

- **Theoretical Analysis:** Proving bounds on approximation error

- **Practical Trade-offs:** When to choose approximation over exact solutions

- **System Integration:** Embedding algorithms in production environments

<hr>

# Run the service
python -m uvicorn logflow-skecher.src.main:app --reload --port 8000 
