import { TestBed } from '@angular/core/testing';

import { TrinoService } from './trino.service';

describe('TrinoService', () => {
  let service: TrinoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TrinoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
