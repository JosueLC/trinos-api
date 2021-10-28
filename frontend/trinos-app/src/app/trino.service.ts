import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { trino } from './trino'

@Injectable({
  providedIn: 'root'
})
export class TrinoService {

  constructor() { }

  getTrinos(): trino[] {
    return [];
  }
}
