import type { FormFieldTypes } from "~/interfaces/transactions.interface";

export interface IDropdown {
  preSelectedOption?: string;
  mobileIcon: string;
  options: string[];
  label: string;
  forField: FormFieldTypes;
  onSelection: (field: FormFieldTypes, value: string) => void;
}