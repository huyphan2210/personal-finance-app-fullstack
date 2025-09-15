<template>
  <table
    :class="{
      'recurring-bills_table': true,
      'no-data': data.length === 0,
    }"
  >
    <colgroup>
      <col style="width: 60%" />
      <col style="width: 24%" />
      <col style="width: 16%" />
    </colgroup>
    <thead class="recurring-bills_table_head">
      <tr>
        <th>Bill Title</th>
        <th>Due Date</th>
        <th>Amount</th>
      </tr>
    </thead>
    <tbody class="recurring-bills_table_body">
      <tr
        :class="{
          'recurring-bills_table_body_item': true,
          paid: item.paidStatus === SubscriptionPaidStatusEnum.Paid,
          'due-soon': item.paidStatus === SubscriptionPaidStatusEnum.DueSoon,
          unpaid: item.paidStatus === SubscriptionPaidStatusEnum.Unpaid,
          upcoming: item.paidStatus === SubscriptionPaidStatusEnum.Upcoming,
        }"
        v-for="item in data"
      >
        <td class="recurring-bills_table_body_item_name">
          <figure>
            <img :src="item.avatarUrl" loading="lazy" :alt="item.user" />
            <figcaption>
              {{ item.user }}
            </figcaption>
          </figure>
          <span>
            {{ transformSubscriptionDueDate(item) }}
            <svg
              v-if="item.paidStatus !== SubscriptionPaidStatusEnum.Upcoming"
              width="14"
              height="14"
              viewBox="0 0 14 14"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                :d="
                  item.paidStatus === SubscriptionPaidStatusEnum.Paid
                    ? 'M7 0.5C5.71442 0.5 4.45772 0.881218 3.3888 1.59545C2.31988 2.30968 1.48676 3.32484 0.994786 4.51256C0.502816 5.70028 0.374095 7.00721 0.624899 8.26809C0.875703 9.52896 1.49477 10.6872 2.40381 11.5962C3.31285 12.5052 4.47104 13.1243 5.73192 13.3751C6.99279 13.6259 8.29973 13.4972 9.48744 13.0052C10.6752 12.5132 11.6903 11.6801 12.4046 10.6112C13.1188 9.54229 13.5 8.28558 13.5 7C13.4982 5.27665 12.8128 3.62441 11.5942 2.40582C10.3756 1.18722 8.72335 0.50182 7 0.5ZM9.85375 5.85375L6.35375 9.35375C6.30732 9.40024 6.25217 9.43712 6.19147 9.46228C6.13077 9.48744 6.06571 9.50039 6 9.50039C5.9343 9.50039 5.86923 9.48744 5.80853 9.46228C5.74783 9.43712 5.69269 9.40024 5.64625 9.35375L4.14625 7.85375C4.05243 7.75993 3.99972 7.63268 3.99972 7.5C3.99972 7.36732 4.05243 7.24007 4.14625 7.14625C4.24007 7.05243 4.36732 6.99972 4.5 6.99972C4.63268 6.99972 4.75993 7.05243 4.85375 7.14625L6 8.29313L9.14625 5.14625C9.19271 5.09979 9.24786 5.06294 9.30855 5.0378C9.36925 5.01266 9.43431 4.99972 9.5 4.99972C9.5657 4.99972 9.63075 5.01266 9.69145 5.0378C9.75215 5.06294 9.8073 5.09979 9.85375 5.14625C9.90021 5.1927 9.93706 5.24786 9.9622 5.30855C9.98734 5.36925 10.0003 5.4343 10.0003 5.5C10.0003 5.5657 9.98734 5.63075 9.9622 5.69145C9.93706 5.75214 9.90021 5.8073 9.85375 5.85375Z'
                    : 'M7 0.5C5.71442 0.5 4.45772 0.881218 3.3888 1.59545C2.31988 2.30968 1.48676 3.32484 0.994786 4.51256C0.502816 5.70028 0.374095 7.00721 0.624899 8.26809C0.875703 9.52896 1.49477 10.6872 2.40381 11.5962C3.31285 12.5052 4.47104 13.1243 5.73192 13.3751C6.99279 13.6259 8.29973 13.4972 9.48744 13.0052C10.6752 12.5132 11.6903 11.6801 12.4046 10.6112C13.1188 9.54229 13.5 8.28558 13.5 7C13.4982 5.27665 12.8128 3.62441 11.5942 2.40582C10.3756 1.18722 8.72335 0.50182 7 0.5ZM6.5 4C6.5 3.86739 6.55268 3.74021 6.64645 3.64645C6.74022 3.55268 6.86739 3.5 7 3.5C7.13261 3.5 7.25979 3.55268 7.35356 3.64645C7.44732 3.74021 7.5 3.86739 7.5 4V7.5C7.5 7.63261 7.44732 7.75979 7.35356 7.85355C7.25979 7.94732 7.13261 8 7 8C6.86739 8 6.74022 7.94732 6.64645 7.85355C6.55268 7.75979 6.5 7.63261 6.5 7.5V4ZM7 10.5C6.85167 10.5 6.70666 10.456 6.58333 10.3736C6.45999 10.2912 6.36386 10.1741 6.30709 10.037C6.25033 9.89997 6.23548 9.74917 6.26441 9.60368C6.29335 9.4582 6.36478 9.32456 6.46967 9.21967C6.57456 9.11478 6.7082 9.04335 6.85368 9.01441C6.99917 8.98547 7.14997 9.00033 7.28701 9.05709C7.42406 9.11386 7.54119 9.20999 7.6236 9.33332C7.70602 9.45666 7.75 9.60166 7.75 9.75C7.75 9.94891 7.67098 10.1397 7.53033 10.2803C7.38968 10.421 7.19892 10.5 7 10.5Z'
                "
                :fill="
                  item.paidStatus === SubscriptionPaidStatusEnum.Paid
                    ? 'var(--green)'
                    : item.paidStatus === SubscriptionPaidStatusEnum.DueSoon
                    ? 'var(--gold)'
                    : 'var(--red)'
                "
              />
            </svg>
          </span>
        </td>
        <td class="recurring-bills_table_body_item_date">
          <span>
            {{ transformSubscriptionDueDate(item) }}
            <svg
              v-if="item.paidStatus !== SubscriptionPaidStatusEnum.Upcoming"
              width="14"
              height="14"
              viewBox="0 0 14 14"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                :d="
                  item.paidStatus === SubscriptionPaidStatusEnum.Paid
                    ? 'M7 0.5C5.71442 0.5 4.45772 0.881218 3.3888 1.59545C2.31988 2.30968 1.48676 3.32484 0.994786 4.51256C0.502816 5.70028 0.374095 7.00721 0.624899 8.26809C0.875703 9.52896 1.49477 10.6872 2.40381 11.5962C3.31285 12.5052 4.47104 13.1243 5.73192 13.3751C6.99279 13.6259 8.29973 13.4972 9.48744 13.0052C10.6752 12.5132 11.6903 11.6801 12.4046 10.6112C13.1188 9.54229 13.5 8.28558 13.5 7C13.4982 5.27665 12.8128 3.62441 11.5942 2.40582C10.3756 1.18722 8.72335 0.50182 7 0.5ZM9.85375 5.85375L6.35375 9.35375C6.30732 9.40024 6.25217 9.43712 6.19147 9.46228C6.13077 9.48744 6.06571 9.50039 6 9.50039C5.9343 9.50039 5.86923 9.48744 5.80853 9.46228C5.74783 9.43712 5.69269 9.40024 5.64625 9.35375L4.14625 7.85375C4.05243 7.75993 3.99972 7.63268 3.99972 7.5C3.99972 7.36732 4.05243 7.24007 4.14625 7.14625C4.24007 7.05243 4.36732 6.99972 4.5 6.99972C4.63268 6.99972 4.75993 7.05243 4.85375 7.14625L6 8.29313L9.14625 5.14625C9.19271 5.09979 9.24786 5.06294 9.30855 5.0378C9.36925 5.01266 9.43431 4.99972 9.5 4.99972C9.5657 4.99972 9.63075 5.01266 9.69145 5.0378C9.75215 5.06294 9.8073 5.09979 9.85375 5.14625C9.90021 5.1927 9.93706 5.24786 9.9622 5.30855C9.98734 5.36925 10.0003 5.4343 10.0003 5.5C10.0003 5.5657 9.98734 5.63075 9.9622 5.69145C9.93706 5.75214 9.90021 5.8073 9.85375 5.85375Z'
                    : 'M7 0.5C5.71442 0.5 4.45772 0.881218 3.3888 1.59545C2.31988 2.30968 1.48676 3.32484 0.994786 4.51256C0.502816 5.70028 0.374095 7.00721 0.624899 8.26809C0.875703 9.52896 1.49477 10.6872 2.40381 11.5962C3.31285 12.5052 4.47104 13.1243 5.73192 13.3751C6.99279 13.6259 8.29973 13.4972 9.48744 13.0052C10.6752 12.5132 11.6903 11.6801 12.4046 10.6112C13.1188 9.54229 13.5 8.28558 13.5 7C13.4982 5.27665 12.8128 3.62441 11.5942 2.40582C10.3756 1.18722 8.72335 0.50182 7 0.5ZM6.5 4C6.5 3.86739 6.55268 3.74021 6.64645 3.64645C6.74022 3.55268 6.86739 3.5 7 3.5C7.13261 3.5 7.25979 3.55268 7.35356 3.64645C7.44732 3.74021 7.5 3.86739 7.5 4V7.5C7.5 7.63261 7.44732 7.75979 7.35356 7.85355C7.25979 7.94732 7.13261 8 7 8C6.86739 8 6.74022 7.94732 6.64645 7.85355C6.55268 7.75979 6.5 7.63261 6.5 7.5V4ZM7 10.5C6.85167 10.5 6.70666 10.456 6.58333 10.3736C6.45999 10.2912 6.36386 10.1741 6.30709 10.037C6.25033 9.89997 6.23548 9.74917 6.26441 9.60368C6.29335 9.4582 6.36478 9.32456 6.46967 9.21967C6.57456 9.11478 6.7082 9.04335 6.85368 9.01441C6.99917 8.98547 7.14997 9.00033 7.28701 9.05709C7.42406 9.11386 7.54119 9.20999 7.6236 9.33332C7.70602 9.45666 7.75 9.60166 7.75 9.75C7.75 9.94891 7.67098 10.1397 7.53033 10.2803C7.38968 10.421 7.19892 10.5 7 10.5Z'
                "
                :fill="
                  item.paidStatus === SubscriptionPaidStatusEnum.Paid
                    ? 'var(--green)'
                    : item.paidStatus === SubscriptionPaidStatusEnum.DueSoon
                    ? 'var(--gold)'
                    : 'var(--red)'
                "
              />
            </svg>
          </span>
        </td>
        <td class="recurring-bills_table_body_item_amount">
          <span>{{ enUSFormatter.format(item.amount) }}</span>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script lang="ts" setup>
import {
  SubscriptionPaidStatusEnum,
  SubscriptionRecurrenceEnum,
} from "~/api/data-contracts";
import type {
  ISubscriptionItem,
  ISubscriptionTable,
} from "~/interfaces/subscriptions.interface";

const { data } = defineProps<ISubscriptionTable>();

const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

const transformSubscriptionDueDate = (subscription: ISubscriptionItem) => {
  const date: Date = new Date(subscription.dueDate);
  const options: Intl.DateTimeFormatOptions = {
    day: "2-digit",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  };

  if (subscription.recurrence === SubscriptionRecurrenceEnum.Yearly) {
    options.year = "numeric";
  }
  return date.toLocaleString("en-GB", options);
};
</script>
<style lang="scss" scoped>
.recurring-bills {
  &_table {
    &.is-loading,
    &.no-data {
      flex: 1;
    }

    &.no-data {
      tbody {
        position: relative;
        &::before {
          content: "No Data";
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          @include text-preset-4-bold;
        }
      }
    }

    colgroup {
      display: none;
    }

    table-layout: fixed;
    width: 100%;

    th,
    td {
      text-align: start;
      color: var(--grey-500);
      padding-block: 1.25rem;
      border-bottom: solid 1px var(--grey-100);
      @include text-preset-5;

      &:last-child {
        text-align: end;
      }

      &:not(:last-child):not(:first-child) {
        display: none;
      }
    }

    &_head {
      display: none;
    }

    &_body {
      &_item {
        &:first-child {
          td {
            padding-top: 0;
          }
        }
        &:last-child {
          td {
            padding-bottom: 0;
            border-bottom: none;
          }
        }

        &.paid {
          .recurring-bills_table_body_item_name span,
          .recurring-bills_table_body_item_date,
          .recurring-bills_table_body_item_amount span {
            color: var(--green);
          }
        }

        &.unpaid {
          .recurring-bills_table_body_item_name span,
          .recurring-bills_table_body_item_date,
          .recurring-bills_table_body_item_amount span {
            color: var(--red);
          }
        }

        &.due-soon {
          .recurring-bills_table_body_item_name span,
          .recurring-bills_table_body_item_date,
          .recurring-bills_table_body_item_amount span {
            color: var(--gold);
          }
        }

        &_name {
          figure {
            display: flex;
            align-items: center;
            gap: 1rem;

            img {
              width: 100%;
              max-width: 2rem;
              border-radius: 50%;
            }

            figcaption {
              color: var(--grey-900);
              @include text-preset-4-bold;
            }
          }

          span {
            display: flex;
            align-items: center;
            gap: 9.5px;
            margin-top: 0.5rem;
          }
        }

        &_date {
          span {
            display: flex;
            align-items: center;
            gap: 9.5px;
          }
        }

        &_amount {
          vertical-align: bottom;
          span {
            display: block;
            color: var(--grey-900);
            @include text-preset-4-bold;
          }
        }
      }
    }
  }
}

@media screen and (min-width: 48rem) {
  .recurring-bills {
    &_table {
      colgroup {
        display: table-column-group;
      }

      th,
      td {
        &:not(:last-child):not(:first-child) {
          display: table-cell;
        }
      }

      th {
        padding-block: 0.75rem;
      }

      &_head {
        display: table-header-group;
      }

      &_body {
        &_item {
          &:first-child {
            td {
              padding-top: 1.5rem;
            }
          }

          &_name {
            figure {
              img {
                max-width: 2.5rem;
              }

              figcaption {
                span {
                  display: none;
                  &:first-child {
                    display: unset;
                    margin-bottom: 0;
                  }
                }
              }
            }
            span {
              display: none;
            }
          }

          &_amount {
            vertical-align: middle;
          }
        }
      }
    }
  }
}

@media screen and (min-width: 90rem) {
  .recurring-bills {
    &_table {
      th,
      td {
        &:first-child {
          padding-left: 1rem;
        }
      }

      th {
        padding-block: 0.75rem;
      }
    }
  }
}
</style>
