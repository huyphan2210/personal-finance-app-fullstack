<template>
  <shared-modal
    modal-heading="Add New Budget"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <p>
      Choose a category to set a spending budget. These categories can help you
      monitor spending.
    </p>
    <form @submit="addNewBudget"></form>
  </shared-modal>
</template>
<script lang="ts" setup>
import type { IBudgetAddNewModal } from "~/interfaces/budgets.interface";

const { isShown } = defineProps<IBudgetAddNewModal>();

const onCloseModal = () => {};
const addNewBudget = (e: Event) => {
  e.preventDefault();
};
</script>
<style lang="scss" scoped></style>
