import React from 'react';
import piatti from './piatti.jsx';

const MenuRistorante = () => {
    return (
        <div>
            <h2>Menu del Ristorante</h2>
            <ul>
                {piatti.map(piatto => (
                    <li key={piatto.id} className="list-group-item d-flex justify-content-between">
                        <span>{piatto.nome}</span>
                        <span className="badge bg-success">{piatto.prezzo} €</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MenuRistorante;
