// Import necessary components from react-router-dom and other parts of the application.
import { Link } from "react-router-dom";
import useGlobalReducer from "../hooks/useGlobalReducer";  // Custom hook for accessing the global state.

export const Login = () => {
  // Access the global state and dispatch function using the useGlobalReducer hook.
  const { store, dispatch } = useGlobalReducer()

  return (
    <div className="container mt-5 vh-100">
      <div className="row justify-content-center">
        <div className="col-md-6 border rounded-4">
          <form className="form-group p-4">
            <div className="mb-3">
              <label for="exampleFormControlInput1" className="form-label">Email address</label>
              <input type="email" className="form-control" id="exampleFormControlInput1" placeholder="name@example.com" />
            </div>
            <div className="mb">
              <label for="inputPassword5" className="form-label">Password</label>
              <input type="password" id="inputPassword5" className="form-control" aria-describedby="passwordHelpBlock" />
              <div id="passwordHelpBlock" className="form-text">
                Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
              </div>
            </div>
          </form>
          <span className="mt-2">¿No tienes una cuenta? <Link to="/register">Registrate</Link></span>
        </div>
      </div>
    </div>
  );
};
