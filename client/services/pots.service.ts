import type {
  CreatePot,
  DeletePot,
  Pots,
  UpdatePot,
} from "~/api/data-contracts";
import { PotModalTypeEnum } from "~/interfaces/pots.interface";
import { handleGetResponse, potsApi } from "./base.service";

export const getPots = async () => {
  const response = await handleGetResponse<Pots>(potsApi.getPotsApi);
  return response.pots;
};

export const addPot = async (payload: CreatePot) => {
  try {
    await potsApi.postPotsApi(payload);
  } catch (error) {
    const message =
      error instanceof Response ? await error.text() : DEFAULT_ERROR_MESSAGE;
    throw new Error(message);
  }
};

export const updatePot = async (payload: UpdatePot) => {
  try {
    await potsApi.patchPotsApi(payload);
  } catch (error) {
    const message =
      error instanceof Response ? await error.text() : DEFAULT_ERROR_MESSAGE;
    throw new Error(message);
  }
};

export const deletePot = async (payload: DeletePot) => {
  try {
    await potsApi.deletePotsApi(payload);
  } catch (error) {
    const message =
      error instanceof Response ? await error.text() : DEFAULT_ERROR_MESSAGE;
    throw new Error(message);
  }
};

export const potModalHeadings: Record<
  PotModalTypeEnum,
  (potName?: string) => string
> = {
  [PotModalTypeEnum.AddNew]: () => "Add New Pot",
  [PotModalTypeEnum.Edit]: () => "Edit Pot",
  [PotModalTypeEnum.Delete]: (potName) => `Delete '${potName}'?`,
  [PotModalTypeEnum.AddToPot]: (potName) => `Add to '${potName}'`,
  [PotModalTypeEnum.Withdraw]: (potName) => `Withdraw from '${potName}'`,
};

export const potModalInstruction: Record<
  PotModalTypeEnum,
  (value?: string) => string
> = {
  [PotModalTypeEnum.AddNew]: () =>
    "Create a pot to set savings targets. These can help keep you on track as you save for special purchases.",
  [PotModalTypeEnum.Edit]: () =>
    "If your saving targets change, feel free to update your pots.",
  [PotModalTypeEnum.Delete]: () =>
    "Are you sure you want to delete this pot? This action cannot be reversed, and all the data inside it will be removed forever.",
  [PotModalTypeEnum.AddToPot]: (value?: string) =>
    `You can add a maximum of ${value} to the pot.`,
  [PotModalTypeEnum.Withdraw]: (value?: string) =>
    `You can withdraw a maximum of ${value} from the pot.`,
};

export const potModalPrimaryButtonContent: Record<PotModalTypeEnum, string> = {
  [PotModalTypeEnum.AddNew]: "Add Pot",
  [PotModalTypeEnum.Edit]: "Save Changes",
  [PotModalTypeEnum.Delete]: "Yes, Confirm Deletion",
  [PotModalTypeEnum.AddToPot]: "Confirm Addition",
  [PotModalTypeEnum.Withdraw]: "Confirm Addition",
};
