import sys

if __name__ == "__main__":
    match sys.argv[1]:
        case "web":
            import app
            app.run_app()

        case "api":
            from app import dd_api
            print("Creating api")
                    
            

        case "total":
            import app
            from app import dd_api
            


            app.run_app()


        case _:
            import app 
            app.run_app()
