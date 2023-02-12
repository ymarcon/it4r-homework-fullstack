// Canton: the canton data
export interface Canton {
  id: number;
  code: string;
  title: string;
  male: number;
  female: number;
  other: number;
}

// Cantons: a map of Cantons, using Canton's code as a key
export interface Cantons extends Array<Canton> { }
