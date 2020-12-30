- To run the application install all dependecies in requirements.txt file.
- Change directory to src and run command "python main.py run"
- Default localhost is running on port 80.
- The app consist of two services namely, greeting service & version service.
- Greeting service: At "/helloworld" returns "Hello Stranger" and "/helloworld?name=AlfredENeumann" return Alfred E Neumann.
- Version service: Provides repository name and last commit hash
- Test cases are in the "specs" folder. 

For Docker:

- To create the app container go to directory and run the following command.
        docker build -t <Username>/<app-name> <source location> (e.g: "C:\abc\xyz\HttpServiceApp")
- To run the app in run the following command
        docker run -p 80:80 <Username>/<app-name>
