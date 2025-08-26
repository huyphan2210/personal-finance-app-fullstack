import type { Pot } from "~/api/data-contracts";
import type { IContentCardDropdownOption } from "./shared.interface";

export enum PotModalTypeEnum {
  AddNew = 1,
  Edit = 2,
  Delete = 3,
}

export interface IPotContentCard {
  potInfo: Pot;
  dropdownOptions: IContentCardDropdownOption[];
  onEditModal: (pot: Pot) => void;
  onDeleteModal: (pot: Pot) => void;
}
export interface IPotModal {

  isShown: boolean;
  type: PotModalTypeEnum;
  usedPots: Pot[];
}

export interface IEditPotModal extends IPotModal {
  targetPot?: Pot;
}

export interface IDeletePotModal extends IPotModal {
  targetPot?: Pot;
}
