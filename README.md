# HelloWorld Flask Application

A production-ready Flask "Hello World" application with complete CI/CD pipeline.

## Features

- **Flask Web Application**: RESTful API with multiple endpoints
- **Health Checks**: Built-in health monitoring endpoint
- **Docker Support**: Containerized application with multi-stage builds
- **CI/CD Pipeline**: GitHub Actions workflow for automated testing and deployment
- **Security Scanning**: Integrated vulnerability scanning with Trivy
- **Code Quality**: Automated linting, formatting, and testing
- **Load Balancing**: Nginx reverse proxy configuration
- **Production Ready**: Gunicorn WSGI server with proper configuration

## API Endpoints

- `GET /` - Hello World message with metadata
- `GET /health` - Health check endpoint
- `GET /api/info` - Application information and available endpoints

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd HelloWorld
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`

### Docker Deployment

1. **Build and run with Docker**
   ```bash
   docker build -t helloworld-app .
   docker run -p 5000:5000 helloworld-app
   ```

2. **Using Docker Compose** (with Nginx)
   ```bash
   docker-compose up -d
   ```

   The application will be available at `http://localhost`

## Testing

Run the test suite:
```bash
pytest tests/ -v --cov=app
```

## Code Quality

- **Linting**: `flake8 .`
- **Formatting**: `black .`
- **Security**: `bandit -r .`

## CI/CD Pipeline

The GitHub Actions workflow includes:

1. **Testing Stage**
   - Python setup and dependency installation
   - Code linting with flake8
   - Code formatting check with black
   - Unit tests with pytest
   - Coverage reporting

2. **Security Stage**
   - Vulnerability scanning with Trivy
   - Security report upload to GitHub Security tab

3. **Build Stage**
   - Docker image building
   - Container registry push
   - Multi-platform builds

4. **Deployment Stages**
   - Staging deployment (on develop branch)
   - Production deployment (on main branch)

## Environment Variables

- `FLASK_ENV`: Application environment (development/production)
- `PORT`: Application port (default: 5000)

## Production Considerations

- **Logging**: Structured logging with proper log levels
- **Monitoring**: Health check endpoints for load balancers
- **Security**: Non-root user in Docker container
- **Performance**: Gunicorn with multiple workers
- **Scalability**: Nginx reverse proxy for load balancing

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Client      │────│     Nginx       │────│   Flask App     │
│                 │    │  (Port 80)      │    │  (Port 5000)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                              │
                                              ▼
                                       ┌─────────────────┐
                                       │   Health Check  │
                                       │   /health       │
                                       └─────────────────┘
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure they pass
5. Submit a pull request

## License

This project is licensed under the MIT License.
