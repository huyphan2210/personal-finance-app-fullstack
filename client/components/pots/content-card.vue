<template>
  <shared-content-card
    :heading="potInfo.name"
    :color-theme="potInfo.colorTheme"
    :dropdown-options="dropdownOptions.concat(defaultPotDropdownOptions)"
  ></shared-content-card>
</template>
<script lang="ts" setup>
import type { IPotContentCard } from "~/interfaces/pots.interface";
import type { IContentCardDropdownOption } from "~/interfaces/shared.interface";
import { Color } from "~/types/color";

const { potInfo, dropdownOptions, onDeleteModal, onEditModal } =
  defineProps<IPotContentCard>();

const defaultPotDropdownOptions: IContentCardDropdownOption[] = [
  {
    content: "Edit Pot",
    onClick: () => {
      onEditModal(potInfo);
    },
  },
  {
    content: "Delete Pot",
    contentColor: Color.Red,
    onClick: () => {
      onDeleteModal(potInfo);
    },
  },
];
</script>
<style lang="scss" scoped></style>
