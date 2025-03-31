import React, { useContext } from "react";
import { Context } from "../store/appContext";

export const Favorite = () => {
    const { store } = useContext(Context)
    return (
        <div className="card" style={{ width: "18rem" }}>
            <div className="card-body">
                <h5 className="card-title">Bienvenido!</h5>
                <p className="card-text">{store.user}</p>
            </div>
        </div>
    );
}