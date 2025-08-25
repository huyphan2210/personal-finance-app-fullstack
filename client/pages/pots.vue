<template>
  <hgroup class="pots_heading">
    <shared-page-heading />
    <shared-button
      class="pots_headin_button--add-new"
      type="button"
      :appearance="ButtonAppearanceEnum.Primary"
      :on-click="openAddNewModal"
    >
      + Add New Pot
    </shared-button>
  </hgroup>
  <ul
    :class="{
      pots_list: true,
      'is-loading': isLoading,
    }"
  >
    <li v-for="(pot, index) in pots" class="pots_list_item">
      <pots-content-card
        :key="pot.name + index"
        :pot-info="pot"
        :dropdown-options="[]"
        :on-edit-modal="openEditModal"
        :on-delete-modal="openDeleteModal"
      />
    </li>
  </ul>
  <pots-add-new-modal
    v-if="!isLoading"
    :is-shown="currentOpeningModal === PotModalTypeEnum.AddNew"
    :type="PotModalTypeEnum.AddNew"
    :used-pots="pots ?? []"
    v-on:on-close-modal="closeModal"
  />
  <pots-add-new-modal
    v-if="!isLoading"
    :is-shown="currentOpeningModal === PotModalTypeEnum.Edit"
    :type="PotModalTypeEnum.Edit"
    :used-pots="pots ?? []"
    :targetPot="targetPot"
    v-on:on-close-modal="closeModal"
  />
</template>

<script setup lang="ts">
import { type Pot } from "~/api/data-contracts";
import { PotModalTypeEnum } from "~/interfaces/pots.interface";
import { ButtonAppearanceEnum } from "~/interfaces/shared.interface";
import { getPots } from "~/services/pots.service";
const isLoading = ref(true);
const currentOpeningModal = ref<PotModalTypeEnum | undefined>();
const targetPot = ref<Pot | undefined>();
const pots = ref<Pot[]>();
const errorStore = useErrorStore();

const openAddNewModal = () => {
  currentOpeningModal.value = PotModalTypeEnum.AddNew;
};
const openEditModal = (pot: Pot) => {
  targetPot.value = pot;
  currentOpeningModal.value = PotModalTypeEnum.Edit;
};
const openDeleteModal = (pot: Pot) => {};

const closeModal = (fetchModal?: boolean) => {
  currentOpeningModal.value = undefined;
  if (fetchModal) {
    getPots()
      .then((value) => {
        pots.value = value;
      })
      .catch((message) => errorStore.setErrorMessage(message))
      .finally(() => (isLoading.value = false));
  }
};
getPots()
  .then((value) => {
    pots.value = value;
  })
  .catch((message) => errorStore.setErrorMessage(message))
  .finally(() => (isLoading.value = false));
</script>

<style lang="scss" scoped>
.pots {
  &_heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &_list {
    flex: 1;
    list-style-type: none;
    display: grid;
    grid-auto-rows: min-content;
    gap: 1.5rem;
  }
}

@media screen and (min-width: 90rem) {
  .pots {
    &_list {
      grid-template-columns: repeat(2, 1fr);
      &_item {
      }
    }
  }
}
</style>
