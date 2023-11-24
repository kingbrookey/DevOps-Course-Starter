# To-Do-App Project

Welcome to another update to the To-Do-App project delivery!

## Getting Started

These instructions will guide you on how to set up and run tests for the project using Docker.

### Prerequisites

Make sure you have the following installed on your machine:

- Docker: [Get Docker](https://docs.docker.com/get-docker/)

### Setting up GitHub Actions Workflow

To automate the testing process with GitHub Actions, you need to create a workflow file. Follow these steps to create the workflow:

1. **Navigate to the `.github/workflows` Folder and create a new workflow file in yml format:**

    Inside the `.github/workflows` folder, create a new file, for example, `dockerized-tests.yml`.

2. **Edit the Workflow File:**

    Open `dockerized-tests.yml` in a text editor and add the following content:

    ```yaml
    name: Continuous Integration Dockerized Tests

    on:
      push:
        branches:
          - '*'
        paths-ignore:
          - '**/*.md'  # Ignores changes to Markdown files, you can add other file types to ignore

      pull_request:
        paths-ignore:
          - '**/*.md'  # Ignores changes to Markdown files

    jobs:
      build:
        name: Build and Test
        runs-on: ubuntu-latest
        
        services:
          docker:
            image: docker:latest
            ports:
              - 2375:2375

        steps:
          - name: Checkout Code Repository
            uses: actions/checkout@v4

          - name: Build Docker Image for Tests
            run: docker build --target test --tag my-test-image .

          - name: Run all tests
            run: docker run my-test-image

          - name: Run Unit or Integration tests
            run: docker run my-test-image tests_unit

    
    ```

    Make sure to replace `tests_unit` with the actual folder names where your unit and integration tests are located.

4. **Commit and Push:**

    Save the changes and commit the new workflow file to your repository:

    ```bash
    git add .github/workflows/dockerized-tests.yml
    git commit -m "Add GitHub Actions workflow for Dockerized Tests"
    git push
    ```

### Running Tests with Docker

Follow the previous instructions to run the tests using Docker:

1. Clone the Repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

2. Build the Docker Image:

    ```bash
    docker build --target test --tag my-test-image .
    ```

3. Run the Tests:

    ```bash
    docker run my-test-image
    ```

    If you want to run only unit or integration tests, modify the commands accordingly, as described in the previous instructions.

4. View Test Results:

    After running the tests, you should see the results in the console. Any failed tests will be highlighted.
