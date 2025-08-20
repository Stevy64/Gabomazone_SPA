import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProductCard from '../components/ProductCard';

function Home() {
  const [products, setProducts] = useState([]);

  // 📡 Appel API Django au chargement de la page
  useEffect(() => {
    axios.get('http://localhost:8000/api/products/')
      .then(response => {
        setProducts(response.data); // Mettre les produits dans le state
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Bienvenue sur Gabomazone</h1>
      <div className="product-list">
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default Home;
