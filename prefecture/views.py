import copy
import json
from email.mime import image
from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    TemplateView,
    UpdateView,
)

from prefecture.consts import NUM_ALL_PREFECTURES
from prefecture.models import PREFECTURES_CODE, Prefecture, Review


class HomeView(TemplateView):

    template_name = "prefecture/home.html"


class DetailPrefectureView(LoginRequiredMixin, DetailView):
    template_name = "prefecture/prefecture_detail.html"
    model = Prefecture


class ResisterPrefectureView(LoginRequiredMixin, CreateView):
    template_name = "prefecture/prefecture_register.html"
    model = Prefecture
    fields = ("name",)
    success_url = reverse_lazy("mypage")

    def form_valid(self, form):
        form.instance.user = self.request.user

        visited_list = Prefecture.objects.filter(user=self.request.user)
        for vl in visited_list:
            if str(vl) == form.instance.name:
                return render(
                    self.request,
                    "prefecture/prefecture_register.html",
                    {"error": "すでに登録済みの都道府県です。"},
                )

        return super().form_valid(form)


class DeletePrefectureView(LoginRequiredMixin, DeleteView):
    template_name = "prefecture/prefecture_confirm_delete.html"
    model = Prefecture
    success_url = reverse_lazy("mypage")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ("prefecture", "title", "text", "rate", "image")
    template_name = "prefecture/review_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prefecture"] = Prefecture.objects.get(
            pk=self.kwargs["prefecture_id"]
        )
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.image == None:
            form.instance.image = "no_image.png"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "prefecture-detail", kwargs={"pk": self.object.prefecture.id}
        )


class UpdateReviewView(UpdateView):
    model = Review
    fields = ("title", "text", "rate", "image")
    template_name = "prefecture/review_update.html"

    # def form_valid(self, form):
    #     if form.instance.image == None:
    #         form.instance.image = "no_image.png"
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "prefecture-detail", kwargs={"pk": self.object.prefecture.id}
        )


class DeleteReviewView(DeleteView):
    template_name = "prefecture/review_confirm_delete.html"
    model = Review

    def get_success_url(self):
        return reverse(
            "prefecture-detail", kwargs={"pk": self.object.prefecture.id}
        )


@login_required
def mypage_view(request):
    visited_list = Prefecture.objects.filter(user=request.user)
    visited_count = len(visited_list)
    un_visited_count = NUM_ALL_PREFECTURES - visited_count
    copied_prefs = copy.deepcopy(PREFECTURES_CODE)

    un_visited_list = []  # 未訪問の都道府県リスト
    visit_dict = {}  # ポリゴン表示用、jsに渡す用
    for p in copied_prefs:
        un_visited_list.append(p[1])
        visit_dict[p[0]] = p[1]

    for vl in visited_list:
        un_visited_list.remove(str(vl))
        i = 1
        while i <= NUM_ALL_PREFECTURES:
            i_str = str(i)
            if str(vl) == visit_dict[i_str]:
                visit_dict[i_str] = 1
            i += 1

    i = 1
    while i <= NUM_ALL_PREFECTURES:
        i_str = str(i)
        if visit_dict[i_str] != 1:
            visit_dict[i_str] = 0
        i += 1

    prefecture_colour_data = json.dumps(visit_dict)

    return render(
        request,
        "prefecture/mypage.html",
        {
            "visited_list": visited_list,
            "visited_count": visited_count,
            "un_visited_list": un_visited_list,
            "un_visited_count": un_visited_count,
            "prefecture_colour_data": prefecture_colour_data,
        },
    )
