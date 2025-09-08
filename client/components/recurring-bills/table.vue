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
          paid: item.dueDate,
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
          <span>{{ transformDate(item.dueDate) }}</span>
        </td>
        <td class="recurring-bills_table_body_item_date">
          {{ transformDate(item.dueDate) }}
        </td>
        <td class="recurring-bills_table_body_item_amount">
          <span>{{ enUSFormatter.format(item.amount) }}</span>
        </td>
      </tr>
    </tbody>
  </table>
</template>
<script lang="ts" setup>
import type { ISubscriptionTable } from "~/interfaces/subscriptions.interface";

const { data } = defineProps<ISubscriptionTable>();

const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

const transformDate = (dateString: string) => {
  const date: Date = new Date(dateString);
  return date.toLocaleString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
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
            display: block;
            margin-top: 0.5rem;
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
              gap: 9.5px;
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
