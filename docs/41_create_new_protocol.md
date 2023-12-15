# Creating a Research Protocol

[TODO] add some explanations

## Step 1: Setting Up a Project Repository 

1. **Clone the demo-protocol repository**: 
    Start by cloning the demo-protocol provided by ReproNim using the following command in your terminal: 
    ```bash 
    git clone https://github.com/ReproNim/demo-protocol.git 
    ``` 
    This command creates a local copy of the demo-protocol on your computer. 

2. **Rename the project**: 
    Rename the cloned directory to match your project's name. In this example, we'll call it `reproschema-demo`: 
    ```bash 
    mv demo-protocol reproschema-demo cd reproschema-demo 
    ``` 

## Step 2: Create a New Repository on GitHub 

1. **Create a new repository**: 
    
    Visit your GitHub account and create a new repository named `reproschema-demo`. Ensure you do not initialize this new repository with a README, .gitignore, or license file. 

2. **Set up the remote repository**: 
    - Remove the existing origin with the command: 
        ```bash 
        git remote remove origin 
        ``` 
    - Add a new origin, which is the repository you just created on GitHub: 
        ```bash 
        git remote add origin https://github.com/[yourusername]/reproschema-demo.git 
        ``` 
    - Set the default branch to 'main' and push your changes: 
        ```bash 
        git branch -M main git push -u origin main 
        ``` 

3. **Create the gh-pages branch**: 
    - Fetch the latest changes from your repository (if any): 
        ```bash 
        git fetch origin 
        ``` 
    - Create and switch to the new gh-pages branch: 
        ```bash 
        git checkout -b gh-pages 
        ``` 
    This branch allows you to deploy your ReproSchema UI publicly. 

## Step 3: Customizing the Cloned Demo-Protocol 

### Editing the DemoProtocol and README.md 

1. **Rename the DemoProtocol Folder**: 

    Change the folder name 'DemoProtocol' to something more reflective of your project. 

2. **Modify the Schema File**: 
    
    In the 'DemoProtocol' folder, rename `DemoProtocol_schema` to a name of your choice, e.g., `younameit_schema`. Update the "@id" on line 4 from `"@id": "DemoProtocol_schema"` to `"@id": "younameit_schema"`. 

3. **Update the description**: 

    Edit the description field in the schema file (line 9) to align with your research. 

4. **Revise the README.md file**: 

    Update the README.md file to reflect the nature and objectives of your research protocol. 

### Updating the config.js file in the ui-changes/src folder 

1. **Update the schema source Link**: 

    Replace the 'githubSrc' link with the raw content link of your schema. 

2. **Adjust the assetsPublicPath**: 
    
    Change `assetsPublicPath: '/demo-protocol/'` to match your repository's name, e.g., `assetsPublicPath: '/reproschema-demo/'`. Example `config.js` content: 
    ```javascript
    module.exports = {
    /* eslint-disable */
    githubSrc: 'https://raw.githubusercontent.com/[yourusername]/reproschema-demo/main/DemoProtocol/[younameit]_schema',
    banner: 'This is a custom protocol for ReproSchema.',
    startButton: 'Join',
    assetsPublicPath: '/reproschema-demo/',
    backendServer: null
    }
    ``` 

### Update the build_deploy.yml file in the .github/workflows folder 

- **Modify the validation command**: Change the line `reproschema -l DEBUG validate DemoProtocol/DemoProtocol_schema` to reflect your new folder and schema file names, e.g., `reproschema -l DEBUG validate [yourfoldername]/[younameit]_schema`. 

These steps are essential for tailoring the demo-protocol to your research project, ensuring that all links, paths, and descriptions accurately represent your study.