## LogFlow Sketcher

An educational implementation of real-time log analytics using the Space-Saving algorithm. This project demonstrates how theoretical computer science principles solve practical engineering problems in observability and monitoring systems.

## 🎯 Educational Purpose

This project is designed to bridge the gap between **theoretical computer science** and **practical software engineering**. It implements a production-style log analytics system based on real-world scenarios, but with a focus on learning and understanding fundamental algorithms.

### Real-World Context
- **Problem**: Monitoring high-volume API traffic with limited resources
- **Real Solution**: Streaming algorithms used by companies like Google, Netflix, Cloudflare
- **Educational Focus**: Understanding the theory behind these solutions

# Run the service
python -m uvicorn logflow-skecher.src.main:app --reload --port 8000 
