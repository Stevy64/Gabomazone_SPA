import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import ProductDetail from './pages/ProductDetail';
import Cart from './pages/Cart';

function App() {
  return (
    <Router>
      {/* Routes principales de notre SPA */}
      <Routes>
        <Route path="/" element={<Home />} />                  {/* Page d'accueil */}
        <Route path="/product/:id" element={<ProductDetail />} /> {/* Détail produit */}
        <Route path="/cart" element={<Cart />} />             {/* Panier */}
      </Routes>
    </Router>
  );
}

export default App;
