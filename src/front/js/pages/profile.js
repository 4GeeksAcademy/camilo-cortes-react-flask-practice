import React from "react";
import { Favorite } from "../component/favorite";

export const Profile = () => {

    return (
        <div className="text-center mt-5">
            <h1>Profile</h1>
            <div className="d-flex justify-content-center">
                <Favorite />
            </div>
        </div>
    );
};