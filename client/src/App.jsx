
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import { UsuariosPage } from "./pages/UsuariosPage";
import { UsuariosFormPage } from "./pages/UsuariosFormPage";
import { Navigation } from "./components/Navigation";

function App() { 

  return (
      <BrowserRouter>
        <Navigation />
        <Routes>
          <Route path="/" element={< Navigate to="/UsuariosPage" />} />
          <Route path="/usuarios" element={<UsuariosPage />} />
          <Route path="/usuarios-create" element={<UsuariosFormPage />} />

        </Routes>
      </BrowserRouter>
  );
}

export default App;
