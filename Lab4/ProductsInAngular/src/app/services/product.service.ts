import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Product} from '../models/product.model';

@Injectable({
    providedIn: 'root',
})
export class ProductService {
    private apiUrl: string = "http://127.0.0.1:8000/products/";

    constructor(private http: HttpClient) {}

    getProducts(): Observable<Product[]> {
        return this.http.get<Product[]>(this.apiUrl);
    }
}
