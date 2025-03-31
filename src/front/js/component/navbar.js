import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { Link, useNavigate } from "react-router-dom";

export const Navbar = () => {
	const { store, actions } = useContext(Context)
	const handleClick = () => {
		actions.logout()
	}

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					{store.auth ? <Link to="/">
						<button className="btn btn-primary" onClick={handleClick}>logout</button>
					</Link> : null}
				</div>
			</div>
		</nav>
	);
};