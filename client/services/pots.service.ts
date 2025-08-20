import type { Pots } from "~/api/data-contracts";
import { PotModalTypeEnum } from "~/interfaces/pots.interface";
import { handleGetResponse, potsApi } from "./base.service";

export const getPots = async () => {
  const response = await handleGetResponse<Pots>(potsApi.getPotsApi);
  return response.pots;
};

export const potModalHeadings: Record<
  PotModalTypeEnum,
  (potName?: string) => string
> = {
  [PotModalTypeEnum.AddNew]: () => "Add New Pot",
  [PotModalTypeEnum.Edit]: () => "Edit Pot",
  [PotModalTypeEnum.Delete]: (potName) => `Delete '${potName}'?`,
};

export const potModalInstruction: Record<PotModalTypeEnum, string> = {
  [PotModalTypeEnum.AddNew]:
    "Create a pot to set savings targets. These can help keep you on track as you save for special purchases.",
  [PotModalTypeEnum.Edit]:
    "If your saving targets change, feel free to update your pots.",
  [PotModalTypeEnum.Delete]:
    "Are you sure you want to delete this pot? This action cannot be reversed, and all the data inside it will be removed forever.",
};

export const potModalPrimaryButtonContent: Record<PotModalTypeEnum, string> = {
  [PotModalTypeEnum.AddNew]: "Add Pot",
  [PotModalTypeEnum.Edit]: "Save Changes",
  [PotModalTypeEnum.Delete]: "Yes, Confirm Deletion",
};
