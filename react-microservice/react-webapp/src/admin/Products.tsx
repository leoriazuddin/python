import React, {useEffect, useState} from 'react';
import Wrapper from './Wrapper'
import {Product} from '../interfaces/product'

const Products = () => {
    const [products, setProducts] = useState([]);
    useEffect(() => {
        (
            async () => {
                //for some reason http://localhost:8000/api/products is failing
                const response = await fetch('http://jsonplaceholder.typicode.com/users')
                .then(res => res.json())
                .then((result) => {
                        setProducts(result);
                    },
                    (error) => {
                        console.log("Error products --> ", error.message);
                    })
                //const data = await response.json();
//                 console.log(response)
            }
        )();
    }, []);

    return (
        <Wrapper>
            <div>
                <h2>Section title</h2>
                <div className="table-responsive">
                  <table className="table table-striped table-sm">
                    <thead>
                      <tr>
                        <th>Title</th>
                        <th>Image</th>
                        <th>Likes</th>
                        <th>#</th>
                      </tr>
                    </thead>
                    <tbody>
                        {products.map(
                        (p: Product) => {
                          return (<tr key={p.id}>
                                <td>{p.name}</td>
                                <td><img src={p.username} height="180" /></td>
                                <td>{p.email}</td>
                                <td>{p.id}</td>
                              </tr>
                              )
                        })}
                    </tbody>
                  </table>
                </div>
            </div>
          </Wrapper>);
};

export default Products;