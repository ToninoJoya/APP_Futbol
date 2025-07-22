export const Register = () => {


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
                </div>
            </div>
        </div>

    )
}; 