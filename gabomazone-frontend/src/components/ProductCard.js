import React from 'react';
import { Link } from 'react-router-dom';

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>{product.description}</p>
      <p>Prix : {product.price} FCFA</p>
      <Link to={`/product/${product.id}`}>Voir le produit</Link>
    </div>
  );
}

export default ProductCard;
