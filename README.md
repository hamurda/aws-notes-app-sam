# Serverless Note-Taking App Backend

This project demonstrates the basics of AWS serverless architecture by building the backend for a note-taking application. It utilizes AWS services such as API Gateway, Lambda, DynamoDB and AWS SAM (Serverless Application Model) for IaC. Additionally simple CI/CD pipline using AWS CodeCommit and CodePipeline is e set up tp automate deployments. 

## Features
- Serverless architecture
- CRUD operations for notes
- Infrastucture as Code using AWS SAM
- Automated CI/CD pipline with AWS CodeCommit and CodePipeline

## Architecture Diagram and Used Services

![Untitled Diagram drawio](https://github.com/user-attachments/assets/e1a081e7-bfa3-44e2-9a06-65e40d3b20b4)

## Service Descriptions

### AWS API Gateway
- Currently entrypoint for the note-taking app
- Manages routes HTTP requests to Lambda functions
### AWS Lambda
- Handles the business logic for CRUD operations
- Triggered by API Gateway
### AWS DynamoDB
- NoSQL database to store the notes
- NOTES_TABLE has partition key 'user_id' and sort key 'timestamp'
- NOTES_TABLE has also a GSI with the partition key 'note_id'

The project is created using AWS SAM to define the infrastructure with a simple template. It's uploaded to AWS CodeCommit repository and integrated with the cI/CD pipeline. 

### Next Steps
- Adding Amazon Cognito
- Adding Front End for the user. 
