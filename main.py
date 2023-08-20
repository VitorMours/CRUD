import sys

if __name__ == "__main__":
    match sys.argv[1]:
        case "web":
            import app
            app.run_app()

        case "api":
            from app import dd_api
            usuario = dd_api.CharacterCreator({"name":"Jonilson","age":22})
            print(usuario)

        case "total":
            import app
            from app import dd_api

            usuario = dd_api.CharacterCreator({"name": "Jonilson", "age": 22})
            print(usuario)

            app.run_app()
