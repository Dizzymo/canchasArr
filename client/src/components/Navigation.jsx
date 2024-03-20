import { Link } from "react-router-dom";

export function Navigation() {
    return (
        <div>
            <Link to="/usuarios"><h1>Usuarios App</h1></Link>
            
            <Link to="/usuarios-create">create usuario</Link>

        </div>
    )
    
}
 
