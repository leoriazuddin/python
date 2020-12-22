import React, {useEffect} from 'react';
import Wrapper from './Wrapper'

const Products = () => {

    useEffect(() => {
        (
            async () => {
                const response = await fetch("http://localhost:8000/api/products")
                .then(res => res.ok? res : Promise.reject(res))
                .then(res => console.log(res.json()))
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
                        <th>#</th>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                        <th>Header</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1,003</td>
                        <td>Integer</td>
                        <td>nec</td>
                        <td>odio</td>
                        <td>Praesent</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
            </div>
          </Wrapper>);
};

export default Products;