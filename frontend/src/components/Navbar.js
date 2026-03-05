import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function Navbar() {
  const { user, logout } = useContext(AuthContext);

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          FM Chatbot
        </Typography>

        <Button color="inherit" component={Link} to="/">
          Home
        </Button>

        {user && (
          <Button color="inherit" component={Link} to="/admin">
            Admin
          </Button>
        )}

        {user ? (
          <Button color="inherit" onClick={logout}>
            Logout
          </Button>
        ) : (
          <Button color="inherit" component={Link} to="/login">
            Login
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;