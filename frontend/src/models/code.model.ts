// Codes: the built-in codes data
export interface Code {
  id: number;
  code: string;
  canton: string;
}

// Cantons: a map of Cantons, using Canton's code as a key
export interface Codes extends Array<Code> { }
