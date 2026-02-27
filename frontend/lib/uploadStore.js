// lib/uploadStore.ts
import { create } from "zustand";

export const useUploadStore = create((set) => ({
  files: [],
  setFiles: (updater) =>
    set((state) => ({
      files: typeof updater === "function"
        ? updater(state.files)
        : updater,
    })),
  clearFiles: () => set({ files: [] }),
}));