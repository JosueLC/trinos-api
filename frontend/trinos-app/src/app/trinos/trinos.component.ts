import { Component, OnInit } from '@angular/core';
import { trino } from '../trino';
import { TrinoService } from '../trino.service'

@Component({
  selector: 'app-trinos',
  templateUrl: './trinos.component.html',
  styleUrls: ['./trinos.component.css']
})
export class TrinosComponent implements OnInit {

  trinos: trino[] = [];

  constructor(private trinoService: TrinoService) { }

  ngOnInit() {
    this.getTrinos();
  }

  getTrinos(): void {
    this.trinoService.getTrinos()
      .subscribe(trinos => this.trinos = trinos);
  }
  
}
