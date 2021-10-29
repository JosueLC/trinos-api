import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { trino } from './trino'
import { MessageService } from './message.service';


@Injectable({
  providedIn: 'root'
})
export class TrinoService {

  private trinosUrl = '/api/v1/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  /** GET trinos from the server */
  getTrinos(): Observable<trino[]> {
    return this.http.get<trino[]>(this.trinosUrl)
      .pipe(
        tap(_ => this.log('info','fetched trinos')),
        catchError(this.handleError<trino[]>('getTrinos', []))
      );
  }
  
  /** GET trino by id. Return `undefined` when id not found */
  getTrinoNo404<Data>(id: string): Observable<trino> {
    const url = `${this.trinosUrl}/?id=${id}`;
    return this.http.get<trino[]>(url)
      .pipe(
        map(trinos => trinos[0]), // returns a {0|1} element array
        tap(t => {
          const outcome = t ? `fetched` : `did not find`;
          this.log('info',`${outcome} trino id=${id}`);
        }),
        catchError(this.handleError<trino>(`getTrino id=${id}`))
      );
  }

  /** POST a new trino to the server */
  addTrino(trino: trino): Observable<trino> {
    return this.http.post<trino>(this.trinosUrl, trino, this.httpOptions).pipe(
      tap((newTrino: trino) => this.log('info',`added trino w/ id=${newTrino.id}`)),
      catchError(this.handleError<trino>('addTrino'))
    );
  }

  /** DELETE: delete the trino from the server */
  deleteTrino(trino: trino | string): Observable<trino> {
    const id = typeof trino === 'string' ? trino : trino.id;
    const url = `${this.trinosUrl}/${id}`;
    return this.http.delete<trino>(url, this.httpOptions).pipe(
      tap(_ => this.log('info',`deleted trino id=${id}`)),
      catchError(this.handleError<trino>('deleteTrino'))
    );
  }

  /** PUT: update the trino on the server */
  updateTrino(trino: trino): Observable<any> {
    return this.http.put(this.trinosUrl, trino, this.httpOptions).pipe(
      tap(_ => this.log('info',`updated trino id=${trino.id}`)),
      catchError(this.handleError<any>('updateTrino'))
    );
  }
  
  /** Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   * */
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error); // log to console instead
      this.log('error',`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }

  /** Catch all errors */


    /** Log a trinoService message with the MessageService */
  private log(msgClass: string, message: string) {
    this.messageService.add(msgClass, message);
  }
}
